const express=require("express");
const cors=require("cors");

const app=express();

const PORT=5000;

app.use(cors());

app.get("/", (req, res)=>{
    res.send("hi");
    console.log(req);
});

app.post("/submit", (req, res)=>{
    console.log(req);
})

app.listen(PORT, ()=>{
    console.log(`SERVER RUNNING ON ${PORT}!`);
})