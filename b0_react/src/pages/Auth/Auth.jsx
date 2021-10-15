import React, { useState } from 'react'
import axios from 'axios'
import { useHistory } from 'react-router-dom'

import s from './Auth.module.scss'

const Auth = ({ isLoggedIn, setIsLoggedIn }) => {
    const [message, setMessage] = useState(isLoggedIn ? "Log out if you wish" : "Log in or register")
    const [btnMessage, setBtnMessage] = useState(1)
    const [username, setUsername] = useState(null)
    const [password, setPassword] = useState(null)
    const [email, setEmail] = useState(null)
    const history = useHistory()

    const loginHandler = async (e) => {
        e.preventDefault()
        try {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('password', password)
            
            const { data } = await axios.post('rest/token/', formData, {})
            console.log({data})
            localStorage.setItem('token_DRF', data.access)
            setIsLoggedIn(true)
            history.push('/')

        } catch (error) {
            if (error.toJSON().message.includes("401")) {
                setMessage("Improper credentials. Try again.")
            }
            else {
                setMessage("Error Logging in")
            }
        }
    }

    const registerHandler = async (e) => {
        e.preventDefault()
        try {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('password', password)
            formData.append('email', email)
            
            const { data } = await axios.post('rest/register/', formData, {})
            console.log({registerData: data})
            setBtnMessage(1)
        } catch (error) {
            setMessage("There was an error")
            console.log({error})
        }
    }

    const logoutHandler = () => {
        localStorage.removeItem('token_DRF')
        setIsLoggedIn(false)
    }

    const handleToggle = () => {
        setEmail(null)
        setUsername(null)
        setPassword(null)
        setBtnMessage(-btnMessage)
    }


    const btnMessageStr = btnMessage === 1 ? "REGISTER" : "LOG IN"

    return (
        <div>
            <div>Auth: {message}</div>
            {isLoggedIn ?
                <div className={`${s.myButton} ${s.blue}`} onClick={logoutHandler}>LOG OUT</div>
            :
                <div>
                    <div className={`${s.myButton} ${s.blue}`} onClick={handleToggle}>{btnMessageStr}</div>
                    {btnMessage === 1 ?
                        <form key={"form1"} onSubmit={(e) => loginHandler(e)}>
                            <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} value={username}></input>
                            <input type="password" placeholder="password" onChange={(e) => setPassword(e.target.value)} value={password}></input>
                            <input type="submit" className={s.myButton} value = "LOG IN"></input>
                        </form>
                    :
                        <form key={"form2"} onSubmit={(e) => registerHandler(e)}>
                            <input type="text" placeholder="username" onChange={(e) => setUsername(e.target.value)} value={username}></input>
                            <input type="text" placeholder="email" onChange={(e) => setEmail(e.target.value)} value={email}></input>
                            <input type="password" placeholder="password" onChange={(e) => setPassword(e.target.value)} value={password}></input>
                            <input type="submit" className={`${s.myButton} ${s.yellow}`} value = "REGISTER"></input>
                        </form>
                    }
                </div>
            }
        </div>
    )
}

export default Auth;