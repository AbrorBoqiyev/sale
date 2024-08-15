import './style.scss'
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function Blogs(props) {
    const [items, setItems] = useState([])

    useEffect(()=> {
        const fetchIems = async () => {
            const response = await axios.get("http://127.0.0.1:8000/apis/Blog/")
            setItems(response.data)
            console.log(response.data)
        };

        fetchIems();
    }, [])

    return ( 
        <div>
            <h1>Items</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name}:{item.description}</li>
                ))}
            </ul>
        </div>
     );
}

export default Blogs;