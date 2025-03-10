from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET
from django.core.files.uploadedfile import InMemoryUploadedFile
from rembg import remove
from io import BytesIO

@require_GET
def index(request):
    return HttpResponse("hello")

@require_POST
def remove_background(request):
    
    if 'file' not in request.FILES:
        return HttpResponseBadRequest("No file uploaded")
    
    uploaded_file: InMemoryUploadedFile = request.FILES['file']
  
    try:
        # 读取文件内容
        input_data = uploaded_file.read()
      
        # 使用 rembg 处理
        output_data = remove(input_data)
      
        # 构建内存文件流
        output_buffer = BytesIO(output_data)
        output_buffer.seek(0)
      
        # 返回文件流响应
        return FileResponse(
            output_buffer,
            filename="output.png",
            content_type="image/png",
            as_attachment=True
        )
      
    except Exception as e:
        return HttpResponseBadRequest(f"Error processing file: {str(e)}")
