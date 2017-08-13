import React, {Component} from 'react';
import './ExercicesChapterResume.css';
import {Link} from 'react-router-dom';

class ExerciceResume extends Component {
  render() {
    let chapter = this.props.chapter;
    let link = '/exercices/chapitre/' + chapter.id;
    if(chapter.available){
      return (
        <Link to={{pathname:link, state:{chapter: chapter}}}>
          <div className="exercice-resume" style={{backgroundColor: chapter.color}}>
            Exercices du Chapitre {chapter.nb} : {chapter.name} <br />
          </div>
        </Link>
      )
    }
    else{
      return (
        <div className="exercice-resume" style={{backgroundColor: chapter.color, opacity: 0.5}}>
          Exercices du Chapitre {chapter.nb} : {chapter.name} <br /><br/>
          <div style={{color: '#F44336'}}>
          À venir...
          </div>
        </div>
      )
    }
  }
}

export default ExerciceResume
