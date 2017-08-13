import React, {Component} from 'react';
import ExercicesChapterResume from './ExercicesChapterResume.js';
import {server_url} from './config.js';

class ExercicesChaptersList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chapters: []
    }
  }

  componentDidMount() {
    fetch(server_url + 'api/chapter/get_all')
    .then(response => response.json())
    .then(responseJson => {this.setState({chapters: responseJson.result.sort((a,b) => a.nb - b.nb)})});
  }

  render() {
    let rows = [];
    this.state.chapters.forEach((chapter) => {
      rows.push(
        <ExercicesChapterResume chapter={chapter}></ExercicesChapterResume>
      )
    });

    return (
      <div className="container">
        <div id="exercice-list">
          {rows}
        </div>
      </div>
    )
  }
}

export default ExercicesChaptersList
