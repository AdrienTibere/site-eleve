import React, {Component} from 'react';
import './ObjectiveResume.css';
import {Link} from 'react-router-dom';

class ObjectiveResume extends Component {
  render() {
    let obj = this.props.obj;
    let link = '/exercices/objectif/' + obj.id;
    return (
      <Link to={{pathname:link, state:{obj:obj, chapter:this.props.chapter}}}>
        <li style={{backgroundColor: this.props.color}}>
          Objectif {obj.nb} : {obj.name}
        </li>
      </Link>
    )
  }
}

export default ObjectiveResume
