import { useDispatch, useSelector } from "react-redux"
import socketIOClient from 'socket.io-client'
import React, { useEffect } from "react"
import AlertsTable from "./AlertsTable"
import { replayTimeUpdated } from '../redux/index'

const ENDPOINT = 'http://127.0.0.1:5000'

function Alerts()  {
  const alerts = useSelector(state => state.alert.alerts)
  const replay_date = useSelector(state => state.alert.replay_date)
  const dispatch = useDispatch()

  useEffect(() => {
    console.log('date: ', replay_date)
    dispatch({type:'RETRIEVE_ALERTS_ASYNC', payload: replay_date})

    const socket = socketIOClient(ENDPOINT);
    socket.on("connect", () => {
      console.log('Websocket connected!');
    });

    socket.on("replay_time", (time) => {
      dispatch({type: 'alert/replayTimeUpdated', payload: time})
    });

    setInterval(function(){
      socket.emit('get_replay');
    }, 1000);

  }, []);

  useEffect(() => {
    dispatch({type:'RETRIEVE_ALERTS_ASYNC', payload: replay_date})
  }, [replay_date])

  return (
    <div>
      <p>Hello World</p>
        <AlertsTable alerts={alerts.slice(0, 25)}/>
    </div>
  )
}

export default Alerts