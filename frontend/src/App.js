import React, { useState, useEffect } from "react";

import "./App.css";

import Select from "react-select";
import api from "./service";

import MapImage from "./assets/map.jpeg";


function App() {
  const [countries, setCountries] = useState([]);
  const [initialCountry, setInitialCountry] = useState("");
  const [finalCountry, setFinalCountry] = useState("");
  const [result, setResult] = useState([])

  useEffect(()=>{
    const initCountries = async () => {
      const res = await api.get('/countries');
      const parsedCountries = res.data.countries.map((e)=>{
        return {
          value: e,
          label: e
        }
      })
      setCountries(parsedCountries)
    }

    initCountries();
  },[])

  const findPath = async () => {
    const res = await api.post("find_path", {
      source: initialCountry,
      destination: finalCountry
    })
    setResult(res.data.path);
  }

  return (
    <div className="App">
      <h1>Juliana Pereira Valle Gonçalves</h1>
      <img src={MapImage} alt="Map" className="Map" />
      <div className="InputContainer">
        <Select
          options={countries}
          placeholder="País inicial"
          onChange={(e)=>{
              setInitialCountry(e.value);
          }}
          className="InputField"
        />
        <Select
          options={countries}
          placeholder="País final"
          onChange={(e)=>{
              setFinalCountry(e.value);
          }}
          className="InputField"
        />
        <button type="submit" onClick={findPath}>Enviar</button>
      </div>
      <ul>
        {result.map((country)=>(
          <li>{country}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
