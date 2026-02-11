from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from shop.models import Festival, Category, Product, Banner, Coupon
from datetime import date, timedelta
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin user created (username: admin, password: admin123)'))

        # Create test user
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='test123',
                first_name='Test',
                last_name='User',
                phone='9876543210',
                address='123 Test Street, Test City',
                city='Mumbai',
                state='Maharashtra',
                pincode='400001'
            )
            self.stdout.write(self.style.SUCCESS('✓ Test user created (username: testuser, password: test123)'))

        # Create Festivals
        festivals_data = [
            {
                'name': 'Dussehra',
                'slug': 'dussehra',
                'description': 'Celebrate the victory of good over evil with amazing offers!',
                'start_date': date.today() - timedelta(days=5),
                'end_date': date.today() + timedelta(days=10),
                'is_active': True,
                'theme_color': '#FF6B35'
            },
            {
                'name': 'Diwali',
                'slug': 'diwali',
                'description': 'Festival of Lights - Brighten your homes with our exclusive collection!',
                'start_date': date.today() + timedelta(days=15),
                'end_date': date.today() + timedelta(days=30),
                'is_active': False,
                'theme_color': '#FFB800'
            },
            {
                'name': 'Holi',
                'slug': 'holi',
                'description': 'Festival of Colors - Add vibrant colors to your celebrations!',
                'start_date': date.today() + timedelta(days=60),
                'end_date': date.today() + timedelta(days=75),
                'is_active': False,
                'theme_color': '#E91E63'
            },
            {
                'name': 'Christmas',
                'slug': 'christmas',
                'description': 'Merry Christmas - Special gifts and decorations for the holiday season!',
                'start_date': date.today() + timedelta(days=90),
                'end_date': date.today() + timedelta(days=105),
                'is_active': False,
                'theme_color': '#C41E3A'
            },
        ]

        for fest_data in festivals_data:
            Festival.objects.get_or_create(
                slug=fest_data['slug'],
                defaults=fest_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(festivals_data)} festivals'))

        # Create Categories
        categories_data = [
            {'name': 'Clothing', 'slug': 'clothing', 'description': 'Traditional and modern clothing'},
            {'name': 'Electronics', 'slug': 'electronics', 'description': 'Latest electronic gadgets'},
            {'name': 'Home Decor', 'slug': 'home-decor', 'description': 'Beautiful home decorations'},
            {'name': 'Gifts', 'slug': 'gifts', 'description': 'Perfect gifts for festivals'},
            {'name': 'Festival Specials', 'slug': 'festival-specials', 'description': 'Special festival items'},
        ]

        for cat_data in categories_data:
            Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(categories_data)} categories'))

        # Get created objects
        dussehra = Festival.objects.get(slug='dussehra')
        diwali = Festival.objects.get(slug='diwali')
        clothing_cat = Category.objects.get(slug='clothing')
        electronics_cat = Category.objects.get(slug='electronics')
        decor_cat = Category.objects.get(slug='home-decor')
        gifts_cat = Category.objects.get(slug='gifts')

        # Create Products
        products_data = [
            {
                'name': 'Traditional Silk Saree',
                'slug': 'traditional-silk-saree',
                'description': 'Beautiful handwoven silk saree perfect for festival celebrations. Made with premium quality silk and intricate designs.',
                'price': Decimal('5999.00'),
                'discount_price': Decimal('4499.00'),
                'category': clothing_cat,
                'stock': 50,
                'rating': Decimal('4.5'),
                'is_featured': True,
                'is_trending': True,
                'festivals': [dussehra, diwali]
            },
            {
                'name': 'Designer Kurta Set',
                'slug': 'designer-kurta-set',
                'description': 'Elegant designer kurta set for men. Comfortable and stylish for festival occasions.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('2199.00'),
                'category': clothing_cat,
                'stock': 75,
                'rating': Decimal('4.3'),
                'is_featured': True,
                'festivals': [dussehra]
            },
            {
                'name': 'Smart LED TV 43 inch',
                'slug': 'smart-led-tv-43',
                'description': 'Full HD Smart LED TV with built-in WiFi and streaming apps. Perfect for home entertainment.',
                'price': Decimal('25999.00'),
                'discount_price': Decimal('21999.00'),
                'category': electronics_cat,
                'stock': 20,
                'rating': Decimal('4.6'),
                'is_featured': True,
                'is_trending': True,
                'festivals': [dussehra, diwali]
            },
            {
                'name': 'Wireless Bluetooth Headphones',
                'slug': 'wireless-bluetooth-headphones',
                'description': 'Premium wireless headphones with active noise cancellation and 30-hour battery life.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3499.00'),
                'category': electronics_cat,
                'stock': 100,
                'rating': Decimal('4.4'),
                'is_trending': True,
                'festivals': [dussehra]
            },
            {
                'name': 'Decorative Diya Set (12 pieces)',
                'slug': 'decorative-diya-set',
                'description': 'Traditional clay diyas with beautiful designs. Set of 12 pieces perfect for Diwali decoration.',
                'price': Decimal('599.00'),
                'discount_price': Decimal('449.00'),
                'category': decor_cat,
                'stock': 200,
                'rating': Decimal('4.7'),
                'is_featured': True,
                'festivals': [diwali]
            },
            {
                'name': 'Festive Wall Hangings',
                'slug': 'festive-wall-hangings',
                'description': 'Colorful wall hangings to decorate your home for festivals. Handcrafted with premium materials.',
                'price': Decimal('899.00'),
                'discount_price': Decimal('699.00'),
                'category': decor_cat,
                'stock': 80,
                'rating': Decimal('4.2'),
                'festivals': [dussehra, diwali]
            },
            {
                'name': 'Premium Dry Fruits Gift Box',
                'slug': 'premium-dry-fruits-gift-box',
                'description': 'Assorted premium dry fruits in an elegant gift box. Perfect for gifting during festivals.',
                'price': Decimal('1999.00'),
                'discount_price': Decimal('1699.00'),
                'category': gifts_cat,
                'stock': 150,
                'rating': Decimal('4.8'),
                'is_featured': True,
                'is_trending': True,
                'festivals': [dussehra, diwali]
            },
            {
                'name': 'Handcrafted Jewelry Set',
                'slug': 'handcrafted-jewelry-set',
                'description': 'Beautiful handcrafted jewelry set with traditional designs. Includes necklace and earrings.',
                'price': Decimal('3499.00'),
                'discount_price': Decimal('2799.00'),
                'category': gifts_cat,
                'stock': 60,
                'rating': Decimal('4.5'),
                'is_trending': True,
                'festivals': [dussehra]
            },
        ]

        for prod_data in products_data:
            festivals = prod_data.pop('festivals', [])
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults=prod_data
            )
            if created and festivals:
                product.festivals.set(festivals)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(products_data)} products'))

        # Create Coupons
        coupons_data = [
            {
                'code': 'DUSSEHRA25',
                'discount_percentage': 25,
                'festival': dussehra,
                'min_purchase': Decimal('1000.00'),
                'max_discount': Decimal('500.00'),
                'valid_from': date.today(),
                'valid_to': date.today() + timedelta(days=10),
                'is_active': True,
                'usage_limit': 100
            },
            {
                'code': 'FESTIVE50',
                'discount_percentage': 50,
                'festival': dussehra,
                'min_purchase': Decimal('5000.00'),
                'max_discount': Decimal('2000.00'),
                'valid_from': date.today(),
                'valid_to': date.today() + timedelta(days=10),
                'is_active': True,
                'usage_limit': 50
            },
        ]

        for coupon_data in coupons_data:
            Coupon.objects.get_or_create(
                code=coupon_data['code'],
                defaults=coupon_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(coupons_data)} coupons'))

        self.stdout.write(self.style.SUCCESS('\n✓ Sample data populated successfully!'))
        self.stdout.write(self.style.WARNING('\nLogin credentials:'))
        self.stdout.write('  Admin: username=admin, password=admin123')
        self.stdout.write('  User: username=testuser, password=test123')
