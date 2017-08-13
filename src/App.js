import React, { Component } from 'react';
import './App.css';
import Appbar from 'muicss/lib/react/appbar';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import ExercicesChaptersList from './ExercicesChaptersList.js';
import Container from 'muicss/lib/react/container';
import Exercice from './Exercice.js';
import ObjectivesByChapter from './ObjectivesByChapter.js';
import ExercicesByObjective from './ExercicesByObjective.js';

class App extends Component {
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
                  <Link to={'/exercices/'} style={s2}>Exercices</Link>
                </td>
              </tr>
            </tbody>
          </table>
          </Container>
        </Appbar>
        <div id="main">
          <Container>
          <Route exact={true} path="/" render={() => (
            <div>
              <div className="mui--text-display4 welcome">Bienvenue !</div>
              <div className="mui--text-display1 welcome">Vous êtes sur le site du Professeur Tibère<br/>Le site d'aide aux devoirs pour les élèves de lycée</div>
            </div>
          )}/>
          <Route exact={true} path="/exercices/" component={ExercicesChaptersList}/>
          <Route path="/exercices/chapitre/:chapterId" component={ObjectivesByChapter}/>
          <Route path="/exercices/objectif/:objId" component={ExercicesByObjective}/>
          <Route exact={true} path="/exercices/:exId" component={Exercice}/>
          </Container>
        </div>
      </div>
      </Router>
    );
  }
}

export default App;
