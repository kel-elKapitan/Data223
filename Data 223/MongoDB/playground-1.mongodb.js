

use('demo')
db.createCollection('mycollection')


// querying the database
use('demo')
db.inventory.insertMany([
  { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
  { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
  { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
  { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
  { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);



use('demo')
db.inventory.find( {})


use('demo')
db.inventory.find( { status: "A" } )


use('demo')
// status is A and quantity is less than 30
db.inventory.find({status: "A", qty:{$gt: 40 }})


// query for an embedded document
use('demo')
db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } ).


use('demo')
db.inventory.find( { size: { h: 14, w: 21 } } ) // not working, need all fields in the embedded document


use('demo')
db.inventory.find( { 'size.h' : 8.5} ) // using one field in the embedded document using . notation

 

use('sample_airbnb')
// get host_response_rate >= 50 and 2 bedrooms
db.listingsAndReviews.count({ 'bedrooms': 2, 'host.host_response_rate': { $lte: 50 } })

// get host.host_is_super_host is true and address.country is "United States" and address.location.is_location_exact = true
use('sample_airbnb')
db.listingsAndReviews.count({'address.country': "United States", 'host.host_is_superhost': false, 'address.location.is_location_exact': true})

use('demo')
db.inventory2.insertMany([
  { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
  { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
  { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
  { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
  { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
]);


use('demo')
db.inventory2.find( { tags: ["red", "blank"] } ) // only where tags have 2 items are in this order 



use('demo')
// get all tags with only 2 items in the tags array  

db.inventory2.find( { tags: ["red", "blank"] ,tags: {$size: 2} } ) 

// using the $size operator
use('demo')
db.inventory2.find( { tags: { $size: 2 } } ) // tags array contains exactly 2 elements


// dim_cm array contains less at least one element and is less than 50
use('demo')
db.inventory2.find( { dim_cm: { $elemMatch: { $lt: 50, $gt: 15 } } } )


// accessing the first element of the items array using index notation
use('demo')
db.inventory2.find( { 'dim_cm.0': { $lt: 14 } } )


// query to replce a document 
use('demo')


db.inventory2.replaceOne({_id:ObjectId("6464cde0f19225bf52077a10")}, { item: "planner", qty: 1000, tags: ["red", "blank", "plain","green","pink"], dim_cm: [ 14, 21 ] })



// update a document
use('demo')

db.inventory.updateOne(
    { item: "paper" },
    {
      $set: { "size.uom": "cm", status: "P" },
      //$currentDate: { lastModified: true } // keeps a timestamp of when the document was updated
    }
)


use('demo')
db.inventory.updateMany(
            {$set: { "size.uom": "cm", status: "P" }}, // update all documents

            {$currentDate: { lastModified: true }  // keeps a timestamp of when the document was updated
})


// find paper and change quantity to 50
use('demo')

db.inventory.updateOne({item: "paper"}, {$set: {qty: 50, status: "P"}})



db.inventory2.updateMany()
















