import { unzip, strFromU8 } from 'fflate';
import loadBinary from './loadBinary';

class File {
  constructor(name, obj) {
    this.name = name;
    this.obj = obj;
  }

  toString() {
    return strFromU8(this.obj);
  }
}

export default class ZipFile {
  constructor(url) {
    this._loadingError = null;
    this._fileLoadingPromise = loadBinary(url)
      .then(data => {
        this.zipData = new Uint8Array(data);
      })
      .catch(err => {
        this._loadingError = err;
      });
  }

  _getFiles(filter) {
    if (this._loadingError) {
      return Promise.reject(this._loadingError);
    }
    return this._fileLoadingPromise.then(() => {
      return new Promise((resolve, reject) => {
        unzip(this.zipData, { filter }, (err, unzipped) => {
          if (err) {
            reject(err);
            return;
          }
          if (!unzipped) {
            reject('No files found');
            return;
          }
          resolve(Object.entries(unzipped).map(([name, obj]) => new File(name, obj)));
        });
      });
    });
  }

  file(filename) {
    return this._getFiles(file => file.name === filename).then(files => files[0]);
  }
  files(path) {
    return this._getFiles(file => file.name.startsWith(path));
  }
}
