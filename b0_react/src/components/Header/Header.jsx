import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronCircleRight } from '@fortawesome/free-solid-svg-icons'
import { faAmazonPay } from '@fortawesome/free-brands-svg-icons'
import { faCalendarAlt } from '@fortawesome/free-regular-svg-icons'

import s from './Header.module.scss'

const Header = ({ isLoggedIn, uploadedImage }) => {
    const [image, setImage] = useState(null)
    console.log({image})

    useEffect(() => {
        setImage(null)

        const getHikerInfo = async () => {
            try {
                const config = {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token_DRF')}`,
                    }
                }
                const { data } = await axios.get('rest/meQuery/', config)
                console.log({meQuery: data})
                setImage(data.image)
                
            } catch (error) {
                console.log({error})
            }
        }

        getHikerInfo()

    }, [isLoggedIn, uploadedImage])

    return (
        <div>
            Header
            <FontAwesomeIcon icon={faChevronCircleRight} style={{fontSize:'3rem'}} />
            <FontAwesomeIcon icon={faAmazonPay} style={{fontSize:'2rem'}} />
            <FontAwesomeIcon icon={faCalendarAlt} style={{fontSize:'1.3rem'}} />
            <div className={s.navBarContainer}>
                <Link className={s.navLink} to="/">Home</Link>
                <Link className={s.navLink} to="/upload">Upload</Link>
                <Link className={s.navLink} to="/auth">Auth</Link>
                <div className={s.navLink}>
                    <div className={s.imageContainer} style={{backgroundImage:`url(http://localhost:8000${image})`}}></div>
                </div>
            </div>
        </div>
    )
}

export default Header;