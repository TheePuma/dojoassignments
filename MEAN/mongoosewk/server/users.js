var mongoose = require('mongoose');
var User = mongoose.model('User')

module.exports = {
    create: function (req,res){
        console.log('this is the name of the new user', req.params.name);
        var newUser = new User({name: req.params.name});
        newUser.save(function(err){
            if(err){
                console.log('something went wrong')
                res.json(err);
            }
            else{
                console.log('success');
                res.json(newUser);
            }
        })
    }
}