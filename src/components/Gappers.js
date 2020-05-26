import React from "react"
import { useSelector } from "react-redux"

function GappersTable()  {

  const gappers = useSelector(state => state.alert.gappers)

  return (
    <table className="bp3-html-table bp3-html-table-bordered">
      <thead>
      <tr>
        <th>Symbol</th>
        <th>Price</th>
        <th>Float</th>
        <th>Volume</th>
        <th>Gap (Dollars)</th>
        <th>Gap (Percentage)</th>
      </tr>
      </thead>
      <tbody>
      {gappers.map(gapper => (
        <tr key={gapper.price+gapper.time+gapper.symbol}>
          <td>{ gapper.symbol }</td>
          <td>{ gapper.price }</td>
          <td>{ gapper.float }</td>
          <td>{ gapper.volume }</td>
          <td>{ gapper.gap_dollars }</td>
          <td>{ gapper.gap_percentage }</td>
        </tr>
      ))}
      </tbody>
    </table>
  )
}

export default GappersTable
