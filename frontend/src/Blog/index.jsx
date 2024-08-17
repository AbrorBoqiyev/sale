import './style.scss'
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function Blog(props) {
    const [items, setItems] = useState([])
    

    
    useEffect(()=> {
        const fetchIems = async () => {
            const response = await axios.get(`https://reqres.in/api/users?page=2`)
            setItems(response.data.data)
            // console.log(response.data.data)
        };

        fetchIems();  
       
    }, [])

    return ( 
        <div>
            <h1>Items</h1>
            <div className='apiCover'>
                {items.map(item => (
                    <div className='cardItem'>
                        <div key={item.id} className="info">
                            <h3>{item.id} {item.first_name} {item.last_name}</h3>
                            <p>{item.email}</p>
                            <button>view</button>
                        </div>
                        { <img src={item.avatar} width={100} alt="avatartImg" /> }
                    </div>
                  
                ))}
            </div>
        </div>
     );
}

export default Blog;