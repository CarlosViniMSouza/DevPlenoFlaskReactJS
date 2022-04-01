const browserSync = require('browser-sync').create();
const paths = require('./gulp.json');
const vendors = require('../../../gohub-1.0.0/vendors.json');
const { name, version, dependencies } = require('../../../gohub-1.0.0/package.json');

const isIterableArray = (array) => Array.isArray(array) && !!array.length;
const isProd = process.env.MODE === 'PROD';
const baseDir = isProd ? paths.dir.prod : paths.dir.dev;

module.exports = {
  name,
  version: `v${version}`,
  dependencies,
  paths,
  vendors,
  isIterableArray,
  baseDir,
  browserSync,
  isProd,
};
