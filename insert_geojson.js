const connection = new Mongo('mongodb://localhost:27017');
const db = connection.getDB('clinic');
const clinicsColl = db.getCollection('info');

// delete all documents that have a location field
clinicsColl.deleteMany({ location: { $exists: true } });

clinicsColl.updateMany(
  {},
  [
    {
      $set: {
        location: {
          $cond: {
            if: {
              $or: [
                { $eq: ['$StandardLongitude', ''] },
                { $eq: ['$StandardLatitude', ''] },
              ],
            },
            then: null,
            else: {
              type: 'Point',
              coordinates: [
                { $toDouble: '$StandardLongitude' },
                { $toDouble: '$StandardLatitude' },
              ],
            },
          },
        },
      },
    },
  ]
);

clinicsColl.createIndex({ location: '2dsphere' });
