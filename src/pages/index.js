import React from "react"
import { Provider } from "react-redux"
import { store } from '../redux'
import { render } from "react-dom";
import Alerts from '../components/Alerts'
import ReplayTime from '../components/ReplayTime'
import CollapseGappers from '../components/Collapse'




export default () => (
  <Provider store={store}>
    <div>
      <ReplayTime/>
      <Alerts/>
      <CollapseGappers/>
    </div>
  </Provider>
)

