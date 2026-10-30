# AI Lab G5 — Step 2 — Urban Routing
**Repository owner:** Younes Behniya  
**Repository:** `ai-lab-g5-step2-Younes-Behniya`  
**Role:** Design / Data-source selection and license review

## هدف این مخزن
این مخزن خروجی نقش «طراحی» در گام دوم پروژه آزمایشگاه هوش مصنوعی با موضوع مسیریابی شهری شیراز است. هدف آن تحویل تصمیم‌های طراحی، منبع داده، مجوزها، مدل داده و قرارداد روشن به عضو مسئول پیاده‌سازی است.

> این مخزن، بسته طراحی و نمونه‌های کمکی است؛ داده واقعی استخراج‌شده از OSM هنوز در آن قرار نگرفته و محدوده دقیق مطالعه باید با گروه نهایی شود.

## تصمیم پیشنهادی پروژه
از هر سه راهبرد داده پشتیبانی می‌کنیم، اما آن‌ها را با اولویت متفاوت به کار می‌بریم:

1. **داده مصنوعی:** برای تست کنترل‌شده الگوریتم‌ها و حالت‌های مرزی.
2. **نقشه واقعی:** شبکه معابر شیراز از OpenStreetMap.
3. **داده ترکیبی (رویکرد اصلی ارزیابی):** شبکه واقعی OSM به‌علاوه موانع/بسته‌شدن‌های مصنوعی و سناریوهای آزمایشی.

این تصمیم به معنی لزوم ساخت سه سامانه مستقل نیست؛ یک مدل گراف و یک موتور مسیریابی می‌تواند با سه منبع/سناریوی داده کار کند.

## ساختار مخزن
```text
design/       مستندات طراحی و تصمیم‌ها
data/         راهنمای داده‌ها و فراداده؛ فایل واقعی نقشه بعداً اضافه می‌شود
src/          نمونه‌های کمکی و قراردادهای پردازش
```

## ترتیب مطالعه برای عضو پیاده‌سازی
1. `design/project_scope.md`
2. `design/data_collection_strategy.md`
3. `design/data_source_and_license.md`
4. `design/data_schema.md`
5. `design/system_architecture.md`
6. `design/implementation_handoff.md`

## منابع
- OpenStreetMap: https://www.openstreetmap.org/
- OSM copyright & attribution: https://www.openstreetmap.org/copyright
- ODbL: https://opendatacommons.org/licenses/odbl/
- OSMnx documentation: https://osmnx.readthedocs.io/
- NetworkX documentation: https://networkx.org/documentation/stable/
