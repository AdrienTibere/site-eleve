import React, { Component, navigateTo } from 'react';
import './App.css';
import Appbar from 'muicss/lib/react/appbar';
import { HashRouter as Router, Link, Route, Switch } from 'react-router-dom';
import ExercicesChaptersList from './ExercicesChaptersList.js';
import Container from 'muicss/lib/react/container';
import Exercice from './Exercice.js';
import ObjectivesByChapter from './ObjectivesByChapter.js';
import ExercicesByObjective from './ExercicesByObjective.js';
import Button from 'muicss/lib/react/button';
import EnsureLoggedInContainer from './EnsureLoggedIn.js';
import {connect} from 'react-redux';

class App extends Component {
  componentDidUpdate(prevProps) {
    const { dispatch, redirectUrl } = this.props
    const isLoggingOut = prevProps.isLoggedIn && !this.props.isLoggedIn
    const isLoggingIn = !prevProps.isLoggedIn && this.props.isLoggedIn

    if (isLoggingIn) {
      dispatch(navigateTo(redirectUrl))
    } else if (isLoggingOut) {
      // do any kind of cleanup or post-logout redirection here
    }
  }

  render() {
    let s2 = {color: 'white', 'font-size': '18px'};

    return (
      <Router>
      <div className="App">
        <Appbar>
          <Container>
          <table width="100%">
            <tbody>
              <tr>
                <td className="mui--appbar-height" > 
                  <Link to={'/'} style={s2}>Accueil</Link> </td>
                <td className="mui--appbar-height" >
                  <Link to={'/exercices'} style={s2}>Exercices</Link>
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
                  <div className="mui--text-display4 welcome">Bienvenue !</div>
                  <div className="mui--text-display1 welcome" style={{marginBottom: '20px', marginTop: '30px'}}>Vous êtes sur le site du Professeur Tibère<br/>Le site d'aide aux devoirs en mathématiques pour les élèves de lycée</div>
                  <div style={{textAlign: "center"}}>
                    <Button color="primary" size="large" style={{fontSize: '20px'}}>Se connecter</Button>
                  </div>
                </div>
              )}/>
              <EnsureLoggedInContainer>
                <Route exact={true} path="/exercices" component={ExercicesChaptersList}/>
                <Route path="/exercices/chapitre/:chapterId" component={ObjectivesByChapter}/>
                <Route path="/exercices/objectif/:objId" component={ExercicesByObjective}/>
                <Route exact={true} path="/exercices/:exId" component={Exercice}/>
              </EnsureLoggedInContainer>
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
    isLoggedIn: state.loggedIn,
    redirectUrl: state.redirectUrl
  }
}

export default connect(mapStateToProps)(App);
//export default App;
