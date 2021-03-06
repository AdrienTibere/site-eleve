import React, { Component } from 'react';
import './App.css';
import Appbar from 'muicss/lib/react/appbar';
import { HashRouter as Router, Link, Route, Switch } from 'react-router-dom';
import ExercicesChaptersList from './ExercicesChaptersList.js';
import Container from 'muicss/lib/react/container';
import Exercice from './Exercice.js';
import ObjectivesByChapter from './ObjectivesByChapter.js';
import ExercicesByObjective from './ExercicesByObjective.js';
import {connect} from 'react-redux';
//import {fetchLogIn} from './actions'
import ConnectOrRegister from './ConnectOrRegister.js'
import Profile from './Profile.js'
import Dropdown from 'muicss/lib/react/dropdown';
import DropdownItem from 'muicss/lib/react/dropdown-item';
import {logOut} from './actions'
import Divider from 'muicss/lib/react/divider';

class App extends Component {
  constructor(props) {
    super(props);
    this.logout = this.logout.bind(this)
  }

  componentDidMount() {
    //const { dispatch } = this.props;
    //dispatch(fetchLogIn());
  }

  componentDidUpdate(prevProps) {
    //how to setup login and logout
    //const { dispatch, redirectUrl } = this.props
    //const isLoggingOut = prevProps.isLoggedIn && !this.props.isLoggedIn
    //const isLoggingIn = !prevProps.isLoggedIn && this.props.isLoggedIn
    //if (isLoggingIn) {
      //dispatch(navigateTo(redirectUrl))
    //} else if (isLoggingOut) {
      // do any kind of cleanup or post-logout redirection here
    //}
  }

  logout() {
    this.props.dispatch(logOut());
    localStorage.removeItem("authUserToken");
  }

  render() {
    let s2 = {color: 'white', fontSize: '18px'};

    return (
      <Router>
      <div className="App">
        <Appbar>
          <Container>
          <table width="100%">
            <tbody>
              <tr style={{verticalAlign: "middle"}}>
                <td className="mui--appbar-height" > 
                  <Link to={'/'} style={s2}>Accueil</Link> 
                  <span style={{marginLeft: "30px"}}/>
                  <Link to={'/exercices'} style={s2}>Exercices</Link>
                </td>
                <td className="mui--appbar-height" style={{display: this.props.user?"table-cell":"none", textAlign: "right"}}>
                  <Dropdown color="primary" label={this.props.user?this.props.user.username:""}>
                    <DropdownItem link="#/profile">Profil</DropdownItem>
                    <Divider />
                    <DropdownItem link="/" onClick={this.logout}>Déconnexion</DropdownItem>
                  </Dropdown>
                </td>
              </tr>
            </tbody>
          </table>
          </Container>
        </Appbar>
        <div id="main">
          <Container>
            <Switch>
              <Route exact={true} path="/" render={() => (
                <div>
                  <div className="mui--text-display3 welcome">Bienvenue {this.props.user?this.props.user.first_name:""} !</div>
                  <div className="mui--text-display1 welcome" style={{marginBottom: '20px', marginTop: '30px'}}>Tu es sur le site du Professeur Tibère<br/>Le site d'aide aux devoirs en mathématiques pour les élèves de lycée</div>
                  <ConnectOrRegister/>
                </div>
              )}/>
              <Route exact={true} path="/exercices" component={ExercicesChaptersList}/>
              <Route path="/exercices/chapitre/:chapterId" component={ObjectivesByChapter}/>
              <Route path="/exercices/objectif/:objId" component={ExercicesByObjective}/>
              <Route exact={true} path="/exercices/:exId" component={Exercice}/>
              <Route exact={true} path="/profile" component={Profile}/>
              <Route render={() => (
                <div>
                  <div className="mui--text-display1 welcome" style={{marginBottom: '20px', marginTop: '30px'}}>Cette page n'existe pas !</div>
                </div>
              )}/>
            </Switch>
          </Container>
        </div>
      </div>
      </Router>
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

export default connect(mapStateToProps)(App);
//export default App;
