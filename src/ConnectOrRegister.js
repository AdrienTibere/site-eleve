import React from 'react'
import RegisterForm from './RegisterForm.js'
import ConnectForm from './ConnectForm.js'
import Button from 'muicss/lib/react/button';
import {connect} from 'react-redux';

class ConnectOrRegister extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      displayRegisterForm: false,
      displayConnectForm: false
    }

    this.showRegisterForm = this.showRegisterForm.bind(this);
    this.showConnectForm = this.showConnectForm.bind(this);
  }

  showRegisterForm() {
    this.setState({displayConnectForm: false, displayRegisterForm: !this.state.displayRegisterForm});
  }

  showConnectForm() {
    this.setState({displayConnectForm: !this.state.displayConnectForm, displayRegisterForm: false});
  }

  render() {
    return (
      <div style={{display: this.props.user?"none":""}}>
        <div style={{textAlign: "center"}}>
          <Button onClick={this.showConnectForm} color="primary" size="large" style={{fontSize: '20px'}}>Se connecter</Button>
          <Button onClick={this.showRegisterForm} size="large" style={{fontSize: '20px'}}>S'inscrire</Button>
        </div>
        <div style={{display: this.state.displayConnectForm ? 'block':'none', width: '60%', margin: 'auto', minWidth: '400px'}}>
          <ConnectForm display={this.showConnectForm} />
        </div>
        <div style={{display: this.state.displayRegisterForm ? 'block':'none', width: '60%', margin: 'auto', minWidth: '400px'}}>
          <RegisterForm display={this.showRegisterForm} />
        </div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    user: state.user
  }
}

export default connect(mapStateToProps)(ConnectOrRegister)
