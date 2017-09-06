import React from 'react'
import RegisterForm from './RegisterForm.js'
import ConnectForm from './ConnectForm.js'
import Button from 'muicss/lib/react/button';
import {connect} from 'react-redux';
import Timeout from './mixins/settimeout.js'; 

class ConnectOrRegister extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      displayRegisterForm: false,
      displayConnectForm: false,
      displayRegisterNotification: false
    }

    this.showRegisterForm = this.showRegisterForm.bind(this);
    this.showConnectForm = this.showConnectForm.bind(this);
    this.handleRegister = this.handleRegister.bind(this);
  }

  mixins: [SetTimeoutMixin]

  showRegisterForm() {
    this.setState({displayConnectForm: false, displayRegisterForm: !this.state.displayRegisterForm});
  }

  showConnectForm() {
    this.setState({displayConnectForm: !this.state.displayConnectForm, displayRegisterForm: false});
  }

  handleRegister() {
    this.setState({displayRegisterNotification: true})
    this.props.setTimeout(function(){
      this.setState({displayRegisterNotification: false});
    }.bind(this),5000);
  }

  render() {
    return (
      <div>
        <div style={{display: this.props.user?"none":""}}>
          <div style={{textAlign: "center"}}>
            <Button onClick={this.showConnectForm} color="primary" size="large" style={{fontSize: '20px'}}>Se connecter</Button>
            <Button onClick={this.showRegisterForm} size="large" style={{fontSize: '20px'}}>S'inscrire</Button>
          </div>
          <div style={{display: this.state.displayConnectForm ? 'block':'none', width: '60%', margin: 'auto', minWidth: '400px'}}>
            <ConnectForm display={this.showConnectForm} />
          </div>
          <div style={{display: this.state.displayRegisterForm ? 'block':'none', width: '60%', margin: 'auto', minWidth: '400px'}}>
            <RegisterForm display={this.showRegisterForm} handleRegister={this.handleRegister} />
          </div>
        </div>
        <div style={{display: this.state.displayRegisterNotification?"flex":"none", textAlign: "center"}}>
          <div style={{display: "inline-flex", margin:"auto", backgroundColor: "#4CAF50", color: "white", padding: "10px", fontSize: "20px"}}>
            Ton inscription a bien fonctionné et tu es désormais connecté !
          </div>
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

export default connect(mapStateToProps)(Timeout(ConnectOrRegister))
