import './style.scss'
import React, {useEffect, useState, } from 'react';
import axios from 'axios';


function NBU() {
    const [items, setItems] = useState([]);
    const [error, setError] = useState(null);
   
    useEffect(()=> {
            const fetchItems = async () => {
                try {
                    const response = await axios.get("http://127.0.0.1:8000/apis/Blog/")
                    setItems(response.data)
                }
                catch (err) {
                    console.error('error fetching data', err);
                    setError(err)
                }
            }
         
            fetchItems();
        }, [])

    useEffect(() =>{
        console.log('items: ', items)
    }, [items])
   
    return ( 
        <div className="coverNbu">
            <h2 style={{textAlign: 'center'}}>this is working...</h2>
            {items.map(i => (
                <div className="NBU"style={{display:'grid', 'gridTemplateColumns': '15% 1fr', 'padding': '0 60px'}}>
                    <h3>{i.title}: </h3>
                    <p>{i.description}</p>
                </div>
            ))}
        </div>
     );
}

export default NBU;

// import React, { useEffect, useState } from 'react'
// import './style.scss';
// import axios from 'axios'

// function NBU() {
//     const [ data, setData ] = useState([])
//     useEffect(() => {
//       axios.get('https://nbu.uz/uz/exchange-rates/json/')
//       .then(res => setData(res.data))
//       .catch(err => console.log(err));


      
//     }, [])

//   return (
//     <div className="App">
//       <h2>axios header</h2>
//       {
//         data.map((d, i) => {
//           return <p key={i}>{d.name}:{d.price}</p>
//         })
//       }
//     </div>
//   );
// }

// export default NBU;