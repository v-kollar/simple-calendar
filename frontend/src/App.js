import React, { Component } from "react";
import Navbar from "./components/navbar";
import { BrowserRouter as Router } from "react-router-dom";
import axios from "axios";

class App extends Component {
  state = {
    //Static scheduled Events to know if something is wrong.
    scheduledEvents: [
      {
        id: 1,
        title: "Connection lost",
        startDate: "2020-04-10T13:00:00",
        endDate: "2030-04-10T15:00:00",
      },
    ],
    currentDate: new Date(),

    //Connstring with backend
    connString: "http://localhost:5000",
  };

  constructor(props) {
    super(props);
    this.commitChanges = this.commitChanges.bind(this);
  }

  componentDidMount() {
    axios.get(`${this.state.connString}/get`).then((res) => {
      const calTasks = res.data;
      this.setState({ scheduledEvents: calTasks });
    });
  }

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { scheduledEvents } = state;

      if (added) {
        //added = object (title, startDate, endDate)
        console.log(added);
        axios.post(`${this.state.connString}/add`, added).then((res) => {
          const calTasks = res.data;
          this.setState({ scheduledEvents: calTasks });
        });
        console.log("ADDED");
      }

      if (changed) {
        //changed = { Id: object(startDate, endDate) };
        axios
          .put(
            `${this.state.connString}/update/${Object.keys(changed)[0]}`,
            changed[Object.keys(changed)[0]]
          )
          .then((res) => {
            const calTasks = res.data;
            this.setState({ scheduledEvents: calTasks });
          });
        console.log(changed[Object.keys(changed)[0]]);

        console.log("CHANGED");
      }

      if (deleted !== undefined) {
        //deleted = Id
        axios
          .delete(`${this.state.connString}/delete/${deleted}`)
          .then((res) => {
            const calTasks = res.data;
            this.setState({ scheduledEvents: calTasks });
          });
        console.log("DELETED");
      }

      return { scheduledEvents };
    });
  }

  render() {
    return (
      <Router>
        <Navbar
          scheduledEvents={this.state.scheduledEvents}
          currentDate={this.state.currentDate}
          commitChanges={this.commitChanges}
        />
      </Router>
    );
  }
}

export default App;
