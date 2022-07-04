import {useState} from "react";
import styled from 'styled-components'

const StyledIntro = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;

  section {
    border: solid .5px #222;
    border-radius: 3px;
    padding: 50px 20px;

    h1 {

    }

    p {
      .df-preview-parent {
        display: flex;
        flex-wrap: wrap;
        padding: 10px;

        .df-preview {
          color: #f90;
          border: .5px solid #f90;
          padding: 5px;
          border-radius: 3px;
          margin: 2px;

          &:hover {
            transition: 1s;
            transform: scale(1.2);
          }
        }
      }

    }

    img {
      background-color: white;
      max-width: 90%;
      max-height: 400px;
      margin: 50px 0 ;
      &:hover {
        transition: 1s;
        transform: scale(1.2);
      }
    }
  }
`

const Intro = () => {

    const [state, setState] = useState({
        originalDfHeaders: ['id',
            'date',
            'bedrooms',
            'bathrooms',
            'sqft_living',
            'sqft_lot',
            'floors',
            'waterfront',
            'view',
            'condition',
            'grade',
            'sqft_above',
            'sqft_basement',
            'yr_built',
            'yr_renovated',
            'zipcode',
            'lat',
            'long',
            'sqft_living15',
            'sqft_lot15',
            'price']
    })


    const baseDfHeadersRenderer = state.originalDfHeaders.map(header => {
        return <span className={'df-preview'}> {header} </span>
    })
//
    const cleandDfRenderer = state.originalDfHeaders.filter(i => !['date', 'waterfront', 'zipcode', 'lat', 'long', 'id']
        .includes(i)).map(header => {
        return <span className={'df-preview'}> {header} </span>
    })
    return (
        <StyledIntro className={'intro'}>
            <section>
                <h1>1. We Are Trying To Estimate The Real Estate Prices</h1>
                <p>the data source are using was provided by our dear Teachers
                    Data_MidTerm_Project_Real_State_Regression.xls</p>
                <img src="https://www.micro.ai/wp-content/uploads/2020/09/ml-pricing-forecasts.jpg" alt=""/>
            </section>
            <section>
                <h2>2. At the very first stage in order to build the model we had to clean the data </h2>
                <p>our data frame had <span className={'df-preview-parent'}> {baseDfHeadersRenderer}</span> columns</p>

                <img src="https://miro.medium.com/max/500/1*yWFQiGjlgHUVYeh4ELELyw.jpeg" alt=""/>
                <p>and after cleaning<span className={'df-preview-parent'}> {cleandDfRenderer}</span></p>
            </section>
            <section>
                <h2>3. to estimate the price we need to split the price column from the rest as target variable<br/>
                    so by using method of splitting X from Y we did the data splitting
                </h2>
                <p>the dataframe had no outliers but lets imagen this is a dynamic data and it can get updated any
                    moment</p>
                <p>so we need a permanent tools to keep the data clean of outliers, that is why we build a special
                    util <br/>
                    which is able to remove outliers from any dataframe
                </p>
                 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Divide20by4.svg/800px-Divide20by4.svg.png" alt=""/>
            </section>
            <section>
                <h2>4. Our data frame had no categorical column but in case this does not become an issue <br/>
                    we create another utility to split the data to categorical and numerical values
                </h2>
                 <img src="https://numeracyguidedet.global2.vic.edu.au/files/2018/12/C3-Resources_L9-10_Top-Drawer-categorical-and-numerical-data-146ex18.jpg" alt=""/>
            </section>
            <section>
                <h2>5. it was time to train the data so we created another tools special for this goal<br/>
                    we cut 30% of te data for test and 70% to build the model
                </h2>
                    <img src="https://miro.medium.com/max/1135/1*cwEeGqeSP5h5MXFm67lD3w.png" alt=""/>
            </section>
            <section>
                <h2>6. of course some part of out dara had some big numbers and it could affect our result<br/>
                    to solve this issue we scale down the data
                </h2>
                 <img src="https://t1.thpservices.com/previewimage/gallil/5e05a4767d1a43cbb8a78f1f9fd36ee1/wr2291915.jpg" alt=""/>
            </section>
            <section>
                <h1>7. it was time to predict the data and you can check the result blow</h1>
                <img src="/plot1.png" alt=""/>
            </section>
            <section>
                <h2>8. also, we got around 64% R2 score </h2>
                                <img src="https://lumiere-a.akamaihd.net/v1/images/r2-d2-main_f315b094.jpeg?region=247%2C0%2C951%2C536" alt=""/>
            </section>
            <section>
                <h2>9. to understand which keys can affect price the most we created a plot and sort them by priority</h2>
                <img src="/plot2.png" alt=""/>
            </section>
            <section>
                <h1>10. Time to test the model by creating a real world application</h1>
                <p>we used library called Flusk to build a webserver using python</p>
                <p>and for the front-end we usd ReactJs</p>
                <p>
                    now our user is able to fill a form and tell us moder about the property, then we estimate the price
                    and show it to the user
                </p>
                <img src="https://www.mimikama.at/wp-content/uploads/2019/10/guter_boeser_hacker.jpg" alt=""/>
            </section>


        </StyledIntro>
    )
}


export default Intro