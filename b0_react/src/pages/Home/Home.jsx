import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import s from './Home.module.scss'

const Home = () => {
    useEffect(() => {

        const getHikerInfo = async () => {
            try {
                const config = {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token_DRF')}`,
                    }
                }
                const { data } = await axios.get('rest/hikes/', config)
                console.log({data})
                
                // no config to pass in, because you don't need to be authenticated
                let trailID = 1
                const data2 = await axios.get(`rest/hikesOnTrail/${trailID}/`, {})
                console.log({data2: data2.data})

            } catch (error) {
                console.log({error})
            }
        }

        getHikerInfo()

    }, [])

    return (
        <div>Home</div>
    )
}

export default Home;