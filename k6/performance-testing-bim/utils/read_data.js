import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';

/**
 * Lee datos de un archivo CSV.
 */
export function read_data(path_data){
    const csv = open(path_data)
    console.log("me llamaron varias veces")
    return papaparse.parse(csv, { header: true }).data
}