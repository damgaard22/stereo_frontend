import React, { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"

function ReplayTime() {
  const replay_time = useSelector(state => state.alert.replay_time)
  const replay_date = useSelector(state => state.alert.replay_date)

  return(
    <div>
      <p>{ replay_time }</p>
      <p>{ replay_date }</p>
    </div>
  )
}

export default ReplayTime