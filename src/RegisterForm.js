import React, {Component} from 'react';
import Form from 'muicss/lib/react/form';
import Input from 'muicss/lib/react/input';
import Button from 'muicss/lib/react/button';
import Select from 'muicss/lib/react/select';
import Option from 'muicss/lib/react/option';
import {server_url} from './config.js';
import fetch from 'isomorphic-fetch';

class RegisterForm extends Component {
	constructor(props) {
    super(props);

    this.state = {
      displayError: false,
      username: null,
      first_name: null,
      last_name: null,
      email: null,
      password: null,
      classe: '2nde'
    }

    this.register = this.register.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
	}

  register(e) {
    e.preventDefault();
    var formData = new FormData(e.target)
    fetch(server_url + 'api/register',
      {
        method: 'POST',
        body: formData
      })
    .then(response => response.json(),
          error => this.setState({displayError: true}))
    .then(json => {
      if (json) {
        if (json.result) {
          this.props.display();
        }
        else {
          this.setState({displayError: true});
        }
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
        <div style={{display: this.state.displayError? "block":"none", color: "red", marginTop: "10px"}}>
          Il y a eu un problème avec ton inscription.<br/>
          Ce nom d'utilisateur ou cette adresse mail est peut-être déjà utilisé
        </div>
        <Form onSubmit={this.register}>
          <legend>Inscription</legend>
          <Input name ="username" label="Nom d'utilisateur" floatingLabel={true} required={true} onChange={this.handleInputChange} />
          <Input name="first_name" label="Prénom" floatingLabel={true} required={true} onChange={this.handleInputChange} />
          <Input name="last_name" label="Nom" floatingLabel={true} required={true} onChange={this.handleInputChange} />
          <Input name="email" label="Email" floatingLabel={true} type="email" required={true} onChange={this.handleInputChange} />
          <Input name="password" label="Mot de passe" floatingLabel={true} type="password" required={true} onChange={this.handleInputChange} />
          <Select name="classe" label="Classe" defaultValue="2nde" required={true} onChange={this.handleInputChange} >
            <Option value="2nde" label="Classe de 2nde" />
            <Option value="other" label="Autre classe" />
          </Select>
          <Button color="primary">S'incrire</Button>
        </Form> 
      </div>
    );
  }
}

export default RegisterForm;
