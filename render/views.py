from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.http import FileResponse, HttpResponseBadRequest
from django.core.files.uploadedfile import InMemoryUploadedFile
from rembg import remove
from io import BytesIO

def index(request):
    return render(request, 'render/index.html', {})

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
