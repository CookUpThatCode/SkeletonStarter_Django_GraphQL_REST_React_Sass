import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import React, { useState } from 'react'

import Home from '../src/pages/Home/Home'
import Upload from '../src/pages/Upload/Upload'
import Header from '../src/components/Header/Header'
import Auth from '../src/pages/Auth/Auth'

const App = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token_DRF'))
    const [uploadedImage, setUploadedImage] = useState(-1)

    // conflict dev3

    return (
        <Router>
            <Header isLoggedIn={isLoggedIn} uploadedImage={uploadedImage} />
            {isLoggedIn ?
                <Switch>
                    <Route exact path='/' component={Home} />
                    <Route exact path='/upload'>
                        <Upload setUploadedImage={setUploadedImage} uploadedImage={uploadedImage} />
                    </Route>
                    <Route exact path='/auth'>
                        <Auth isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
                    </Route>
                </Switch>
            :
                <Auth isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
            }
        </Router>
     );
}

export default App;



