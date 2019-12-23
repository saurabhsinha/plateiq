1. api localhost:3002/ocr_internal/addDigitized
adding or updating single or multiple data at one time.
sample data - [{
	"invoiceNo": 123433,
	"date": 2225,
	"item": {
		"type": "pens",
		"quantity": 20010
	}
}]

2. api localhost:3001/ocr/uploadPDF
uploading the pdf file to server
sample form data - key: image
value - path to file.

3. api localhost:3001/ocr/getStatus

4. api localhost:3001/ocr/getData
get the data
