import React from "react"
import { Collapse } from "@blueprintjs/core";
import { Button } from "@blueprintjs/core";
import { Pre } from "@blueprintjs/core";
import GappersTable from "./Gappers"


class CollapseGappers extends React.Component {
  state = {
    isOpen: false,
  };

  render() {
    return (
      <div>
        <Button onClick={this.handleClick}>
          {this.state.isOpen ? "Hide" : "Show"}  Gappers
        </Button>
        <Collapse isOpen={this.state.isOpen}>
          <GappersTable/>
        </Collapse>
      </div>
    );
  }

  handleClick = () => {
    this.setState({ isOpen: !this.state.isOpen });
  }
}

export default CollapseGappers