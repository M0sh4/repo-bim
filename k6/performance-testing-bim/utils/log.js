export function log_req_res(request, response, context){
    console.log("vu:", __VU, "iter:" , __ITER, "context:", context, "Request:", request)
    console.log("vu:", __VU, "iter:" , __ITER, "context:", context, "Response:", response)
}