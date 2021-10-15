import React, { useState } from 'react'
import axios from 'axios'

import s from './Upload.module.scss'

const Upload = ({ setUploadedImage, uploadedImage }) => {
    const [message, setMessage] = useState("Upload file please")
    const [file, setFile] = useState(null)

    console.log({file})

    const fileHandler = (e) => {
        const f = e.target.files[0]
        setFile(f)
    }

    const uploadHandler = async (e) => {
        e.preventDefault()
        const formData = new FormData()
        formData.append('image', file)
        formData.append('hikerID', 2)

        try {
            const config = {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token_DRF')}`,
                    'Content-Type': 'multipart/form-data',
                }
            }
            const { data } = await axios.post('rest/uploadImage/', formData, config)
            setMessage(data)
            setUploadedImage(uploadedImage*-1)
        } catch (error) {
            setMessage("Error uploading file")
        }
    }

    return (
        <div>
            <div>Upload: {message}</div>
            <form onSubmit={(e) => uploadHandler(e)}>
                <input type="file" accept="image/*" onChange={(e) => fileHandler(e)} />
                <input type="submit" value="DO IT NOW" className={s.myButton} />
            </form>
        </div>
    );
}

export default Upload;

