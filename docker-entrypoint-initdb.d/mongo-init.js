print('Start #################################################################');

db = db.getSiblingDB('testDB');
db.createUser(
  {
    user: 'mongoadmin',
    pwd: 'mongoadmin',
    roles: [{ role: 'readWrite', db: 'testDB' }],
  },
);
db.createCollection('users');

print('END #################################################################');
