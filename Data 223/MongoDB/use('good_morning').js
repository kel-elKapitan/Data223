use('good_morning')

db.createCollection('beautiful_day')

use('sample_airbnb')
db.listingsAndReviews.count({beds:{$in:[2,4]}})
