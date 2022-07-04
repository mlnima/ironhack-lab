import styled from 'styled-components'
import './App.css'
import {useState} from "react";
import axios from 'axios';
import Intro from './components/Intro'

const StyledApp = styled.div`

  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;

  h1{
    span{
      color: #f90;
    }
  }
  form {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 600px;
    height: 600px;
    grid-gap: 10px;

    .form-field {
      width: 300px;
      display: flex;
      justify-content: space-between;
      align-items: center;

      input {
        display: block;
        width: 80%;
        padding: 0.375rem 0.75rem;
        font-size: 1rem;
        line-height: 1.5;
        color: #495057;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: 0.25rem;
        transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
        margin: 5px;
      }
    }
    
    button {
    display: inline-block;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.25rem;
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

  }
`

const App = () => {

    const [state, setState] = useState({
        estimatedPrice: 0
    })
    const [formData, setFormData] = useState({
        bedrooms: 2,
        bathrooms: 1,
        sqft_living: 500,
        sqft_lot: 10,
        floors: 1,
        yr_built: 2000,
        view: 2,
        condation: 2,
        grade: 7,
        sqft_above: 20,
        sqft_basement: 3,
        yr_renovated: 2000,
        sqft_living15: 1000,
        sqft_lot15: 1200
    })

    const onChangeHandler = (e) => {
        console.log([e.target.name], e.target.value)
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const onSubmitHandler = (e) => {
        e.preventDefault()
        axios.post('/api/estimatePrice', formData).then(res => {
            setState({
                ...state,
                estimatedPrice: res.data?.estimate_price
            })
        })
    }


    const renderFields = Object.keys(formData).map(field => {
        return (
            <div className={'form-field'}>
                <p>{field}</p>
                <input type="text" name={field} value={formData[field]} onChange={e => onChangeHandler(e)}/>
            </div>
        )
    })

    return (
        <StyledApp className="App">
            <Intro/>
            <h1>Estimated Price of your property : <span>{state.estimatedPrice}$ </span></h1>
            <form onSubmit={e => onSubmitHandler(e)}>
                {renderFields}
                <button type='submit'>Calculate</button>
            </form>
        </StyledApp>
    );
}

export default App;
