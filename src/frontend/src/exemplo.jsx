import React from 'react'

function App(){
  return (
    <>
      <div>
        <div className="homebutton-dummy-container">
          <button className="homebutton-homebutton">
            <img
              src="/playground_assets/rectangle113-b0r-200w.png"
              alt="Rectangle113"
              className="homebutton-rectangle1"
            />
            <img
              src="/playground_assets/logo14-ufkj-200w.png"
              alt="Logo14"
              className="homebutton-logo"
            />
            <img
              src="/playground_assets/usericon1button15-j55l-200h.png"
              alt="usericon1button15"
              className="homebutton-usericon1button"
            />
            <img
              src="/playground_assets/reportsicon116-m6vq-200w.png"
              alt="Reportsicon116"
              className="homebutton-reportsicon1"
            />
            <span className="homebutton-text">
              <span>
                Quarta 12:30
                <span
                  dangerouslySetInnerHTML={{
                    __html: ' ',
                  }}
                />
              </span>
            </span>
            <span className="homebutton-text02">
              <span>17/03/2023</span>
            </span>
            <div className="homebutton-group27">
              <div className="homebutton-group15">
                <img
                  src="/playground_assets/image1186-zuf8-300w.png"
                  alt="image1186"
                  className="homebutton-image1"
                />
                <span className="homebutton-text04">
                  <span>Nome</span>
                </span>
                <div className="homebutton-group14">
                  <span className="homebutton-text06">
                    <span>Ensaios Realizados:</span>
                  </span>
                  <span className="homebutton-text08">
                    <span>Numero</span>
                  </span>
                </div>
                <div className="homebutton-group13">
                  <span className="homebutton-text10">
                    <span>Email:</span>
                  </span>
                  <span className="homebutton-text12">
                    <span>exemplo@gmail.com</span>
                  </span>
                </div>
                <div className="homebutton-group151">
                  <span className="homebutton-text14">
                    <span>Senha:</span>
                  </span>
                  <span className="homebutton-text16">
                    <span>Senha</span>
                  </span>
                </div>
              </div>
            </div>
          </button>
        </div>
      </div>
      <style jsx>
        {`
          .homebutton-dummy-container {
            width: 100%;
            height: 900px;
          }
          .homebutton-homebutton {
            width: 100%;
            height: 1024px;
            display: flex;
            overflow: hidden;
            position: relative;
            align-items: flex-start;
            flex-shrink: 0;
            border-color: transparent;
            background-color: rgba(255, 255, 255, 1);
          }
          .homebutton-rectangle1 {
            top: 0px;
            left: 0px;
            width: 116px;
            height: 1024px;
            position: absolute;
            border-color: transparent;
          }
          .homebutton-logo {
            top: 40px;
            left: 29px;
            width: 58px;
            height: 59px;
            position: absolute;
            border-color: transparent;
          }
          .homebutton-usericon1button {
            top: 931px;
            left: 31px;
            width: 55px;
            height: 55px;
            position: absolute;
            border-color: transparent;
          }
          .homebutton-reportsicon1 {
            top: 166px;
            left: 30px;
            width: 57px;
            height: 59px;
            position: absolute;
            border-color: transparent;
          }
          .homebutton-text {
            top: 38px;
            left: 1289px;
            color: rgba(0, 0, 0, 1);
            height: auto;
            position: absolute;
            font-size: 15px;
            align-self: auto;
            font-style: Regular;
            text-align: left;
            font-family: Montserrat;
            font-weight: 400;
            line-height: normal;
            font-stretch: normal;
            margin-right: 0;
            margin-bottom: 0;
            text-decoration: none;
          }
          .homebutton-text02 {
            top: 38px;
            left: 173px;
            color: rgba(0, 0, 0, 1);
            height: auto;
            position: absolute;
            font-size: 15px;
            align-self: auto;
            font-style: Regular;
            text-align: left;
            font-family: Montserrat;
            font-weight: 400;
            line-height: normal;
            font-stretch: normal;
            margin-right: 0;
            margin-bottom: 0;
            text-decoration: none;
          }
          .homebutton-group27 {
            top: 144px;
            left: 173px;
            width: 1129.71728515625px;
            height: 698.115478515625px;
            display: flex;
            padding: 0;
            position: absolute;
            align-self: auto;
            box-sizing: border-box;
            align-items: flex-start;
            flex-shrink: 1;
            border-color: transparent;
            border-style: none;
            border-width: 0;
            margin-right: 0;
            border-radius: 0px 0px 0px 0px;
            margin-bottom: 0;
            flex-direction: row;
            justify-content: flex-start;
            background-color: transparent;
          }
          .homebutton-group15 {
            top: -7px;
            left: -34px;
            width: 1129.71728515625px;
            height: 698.115478515625px;
            display: flex;
            padding: 0;
            position: absolute;
            align-self: auto;
            box-sizing: border-box;
            align-items: flex-start;
            flex-shrink: 1;
            border-color: transparent;
            border-style: none;
            border-width: 0;
            border-radius: 0px 0px 0px 0px;
            flex-direction: row;
            justify-content: flex-start;
            background-color: transparent;
          }
          .homebutton-image1 {
            top: 0px;
            left: 0px;
            width: 274px;
            height: 275px;
            position: absolute;
            border-color: transparent;
          }
          .homebutton-text04 {
            top: 85px;
            left: 434px;
            color: rgba(0, 0, 0, 1);
            width: 547px;
            height: auto;
            position: absolute;
            font-size: 55px;
            align-self: auto;
            font-style: Bold;
            text-align: left;
            font-family: Montserrat;
            font-weight: 700;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-group14 {
            top: 493px;
            left: 434px;
            width: 695.71728515625px;
            height: 43.329524993896484px;
            display: flex;
            padding: 0;
            position: absolute;
            align-self: auto;
            box-sizing: border-box;
            align-items: flex-start;
            flex-shrink: 1;
            border-color: transparent;
            border-style: none;
            border-width: 0;
            border-radius: 0px 0px 0px 0px;
            flex-direction: row;
            justify-content: flex-start;
            background-color: transparent;
          }
          .homebutton-text06 {
            color: rgba(0, 0, 0, 1);
            width: 386px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Medium;
            text-align: left;
            font-family: Montserrat;
            font-weight: 500;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-text08 {
            top: 0.000005959053851256613px;
            left: 396.3597717285156px;
            color: rgba(0, 0, 0, 1);
            width: 299px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Regular;
            text-align: left;
            font-family: Montserrat;
            font-weight: 400;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-group13 {
            top: 307px;
            left: 434px;
            width: 611.9238891601562px;
            height: 39.73406982421875px;
            display: flex;
            padding: 0;
            position: absolute;
            align-self: auto;
            box-sizing: border-box;
            align-items: flex-start;
            flex-shrink: 1;
            border-color: transparent;
            border-style: none;
            border-width: 0;
            border-radius: 0px 0px 0px 0px;
            flex-direction: row;
            justify-content: flex-start;
            background-color: transparent;
          }
          .homebutton-text10 {
            top: 4.0788984298706055px;
            left: -0.0000444259203504771px;
            color: rgba(0, 0, 0, 1);
            width: 152px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Medium;
            text-align: left;
            font-family: Montserrat;
            font-weight: 500;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-text12 {
            top: 0.000012098685147066135px;
            left: 214.5706787109375px;
            color: rgba(0, 0, 0, 1);
            width: 397px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Regular;
            text-align: left;
            font-family: Montserrat;
            font-weight: 400;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-group151 {
            top: 662px;
            left: 434px;
            width: 430.08056640625px;
            height: 36.11549377441406px;
            display: flex;
            padding: 0;
            position: absolute;
            align-self: auto;
            box-sizing: border-box;
            align-items: flex-start;
            flex-shrink: 1;
            border-color: transparent;
            border-style: none;
            border-width: 0;
            border-radius: 0px 0px 0px 0px;
            flex-direction: row;
            justify-content: flex-start;
            background-color: transparent;
          }
          .homebutton-text14 {
            color: rgba(0, 0, 0, 1);
            width: 173px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Medium;
            text-align: left;
            font-family: Montserrat;
            font-weight: 500;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
          .homebutton-text16 {
            top: 0.46031835675239563px;
            left: 204.6368408203125px;
            color: rgba(0, 0, 0, 1);
            width: 225px;
            height: auto;
            position: absolute;
            font-size: 36px;
            align-self: auto;
            font-style: Regular;
            text-align: left;
            font-family: Montserrat;
            font-weight: 400;
            line-height: normal;
            font-stretch: normal;
            text-decoration: none;
          }
        `}
      </style>
    </>
  )
}

export default App