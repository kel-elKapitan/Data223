use('good_morning')

db.createCollection('beautiful_day')

use('sample_airbnb')
db.listingsAndReviews.count({beds: 4,bedrooms:2})


use('sample_airbnb')
db.listingsAndReviews.find({beds: 4,bedrooms:2})

// list the collections in the database
use('sample_airbnb')    
db.getCollectionNames()