import React from 'react'
import {
    BrowserRouter,
    Route,
    Routes,
} from "react-router-dom";


import Simplest from './modules/simplest';


export default function D6Routes() {
    return (
        <BrowserRouter path="pisdev">
            <Routes>
                <Route path="/pisdev/test" element={<Simplest />} />
            </Routes>
        </BrowserRouter>
    )
}
