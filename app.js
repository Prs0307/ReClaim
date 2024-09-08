const express = require('express');
const path = require('path');
const app = express();

// Set the view engine to EJS
app.set("view engine", 'ejs');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.render("home");
});

app.post('/result', (req, res) => {
    res.render('result', {
      category: req.body.category,
      make: req.body.make,
      brand: req.body.brand,
      model: req.body.model,
      condition: req.body.condition
    });
  });

app.get('/signup', (req, res) => {
    res.render("signup");
})

app.get('/login', (req, res) => {
    res.render("login");
})

app.post('/address', (req, res) => {
    res.render('nearby_shop');
  });

app.post('/address', (req, res) => {
    res.render('nearby_shop');
  });

app.get('/appointment', (req, res) => {
    res.render('appointment');
  });


// Listen on port 3000

app.listen(3000);
