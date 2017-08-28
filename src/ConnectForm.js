import React, {Component} from 'react';
import Form from 'muicss/lib/react/form';
import Input from 'muicss/lib/react/input';
import Button from 'muicss/lib/react/button';
import {server_url} from './config.js';
import fetch from 'isomorphic-fetch';
import {connect} from 'react-redux';
import {logIn} from './actions'

class ConnectForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      displayError: false,
      username: null,
      password: null
    }
    this.login = this.login.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  login(e) {
    e.preventDefault();
    var formData = new FormData(e.target);
    fetch(server_url + 'api/login',
      {
        method: 'POST',
        body: formData
      })
    .then(response => response.json())
    .then(json => {
      if (json.result) {
        this.setState({displayError: false});
        this.props.display();
        this.props.dispatch(logIn(json.user));
      }
      else {
        this.setState({displayError: true});
      }
    });
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }

  render() {
    return (
      <div>
        <div style={{display: this.state.displayError? "block":"none", color:"red", marginTop: "10px"}}>
          Il y a eu un problème avec ta connexion. Vérifie ton identifiant et ton mot de passe.
        </div>
        <Form onSubmit={this.login}>
          <legend>Connexion</legend>
          <Input name="username" label="Nom d'utilisateur" floatingLabel={true} required={true} onChange={this.handleInputChange} />
          <Input name="password" label="Mot de passe" floatingLabel={true} required={true} onChange={this.handleInputChange} />
          <Button color="primary">Se connecter</Button>
        </Form> 
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    isLoggedIn: state.isLoggedIn,
    redirectUrl: state.redirectUrl,
    user: state.user
  }
}

export default connect(mapStateToProps)(ConnectForm);
