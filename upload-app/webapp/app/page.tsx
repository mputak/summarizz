"use client"

import { ChangeEvent, useState } from "react"


const apiURL = "http://pyapi:5000"  // TODO Replace this with environment var


export default function Home() {
  const [file, setFile] = useState<File>()
  console.log("API URL " + apiURL)
  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0])
    }
  }

  const handleUpload = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault()
    if (!file) return

    try {
      const res = await fetch(`${apiURL}/upload-url`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ filename: file.name }) 
      });
      const data = await res.json()
      
      const uploadRes = await fetch(data.url, {
        method: 'PUT',
        headers: {
          'Content-Type': file.type,
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Request-Method': 'PUT'
        },
        body: file
      })

      if (!uploadRes.ok) {
        alert('Upload failed')
      }

      alert('Upload success')

      setFile(undefined)

    } catch (err) {
      alert(err)
    }
  }


  return (
    <main>
      <form>
        <label>
          Upload a file:
          <br />
          <input type="file" onChange={handleFileChange}/>
        </label>
        <br />
        <div>{file && `${file.name} - ${file?.type}`}</div>
        <button onClick={handleUpload}>Upload</button>
      </form>
    </main>
  )
}
