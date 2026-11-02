import math

from js import document, window
from pyodide.ffi import create_proxy


canvas = document.getElementById("kaleidoscope")
context = canvas.getContext("2d")
slices = 14
slice_angle = math.tau / slices


def resize_canvas(_event=None):
    pixel_ratio = window.devicePixelRatio or 1
    width = canvas.clientWidth
    height = canvas.clientHeight
    canvas.width = round(width * pixel_ratio)
    canvas.height = round(height * pixel_ratio)
    context.setTransform(pixel_ratio, 0, 0, pixel_ratio, 0, 0)


def draw_pattern(timestamp):
    width = canvas.clientWidth
    height = canvas.clientHeight
    center_x = width / 2
    center_y = height / 2
    radius = min(width, height) * 0.46
    time = timestamp / 1000

    context.clearRect(0, 0, width, height)
    context.save()
    context.translate(center_x, center_y)

    for index in range(slices):
        context.save()
        context.rotate(index * slice_angle + time * 0.12)
        context.beginPath()
        context.moveTo(0, 0)
        context.arc(0, 0, radius, -slice_angle / 2, slice_angle / 2)
        context.closePath()
        context.clip()
        if index % 2:
            context.scale(1, -1)

        hue = (index * 27 + time * 24) % 360
        context.lineWidth = max(1, radius * 0.008)

        for ring in range(1, 7):
            distance = radius * ring / 7
            pulse = math.sin(time * 1.4 + ring * 0.8) * radius * 0.025
            point_a = distance + pulse
            point_b = distance * 0.72 - pulse

            context.beginPath()
            context.moveTo(0, 0)
            context.quadraticCurveTo(point_a * 0.55, point_b, point_a, 0)
            context.quadraticCurveTo(point_a * 0.55, -point_b, 0, 0)
            context.strokeStyle = f"hsla({hue + ring * 13}, 90%, 72%, 0.8)"
            context.stroke()

            context.beginPath()
            context.arc(point_a, 0, max(2, radius * 0.018), 0, math.tau)
            context.fillStyle = f"hsl({hue + ring * 19}, 95%, 78%)"
            context.fill()

        context.restore()

    context.restore()
    window.requestAnimationFrame(animation_frame)


resize_canvas()
window.addEventListener("resize", create_proxy(resize_canvas))
animation_frame = create_proxy(draw_pattern)
window.requestAnimationFrame(animation_frame)
