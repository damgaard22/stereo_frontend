import React from "react"

function AlertsTable(props)  {

  return (
    <table className="bp3-html-table bp3-html-table-bordered">
      <thead>
      <tr>
        <th>Time</th>
        <th>Symbol</th>
        <th>Price</th>
        <th>Float</th>
        <th>Volume</th>
        <th>Rel Volume</th>
        <th>Change %</th>
      </tr>
      </thead>
      <tbody>
      {props.alerts.map(alert => (
        <tr key={alert.price+alert.time+alert.symbol}>
          <td>{ alert.time }</td>
          <td>{ alert.symbol }</td>
          <td>{ alert.price }</td>
          <td>{ alert.float }</td>
          <td>{ alert.volume }</td>
          <td>{ alert.relative_volume }</td>
          <td>{ alert.change }</td>
        </tr>
      ))}
      </tbody>
    </table>
  )
}

export default AlertsTable
