# Maintainer: David-Alexandre Rancourt <david.a.rancourt@gmail.com>

pkgname=dwm-status
pkgrel=1
pkgver=2.0.5
pkgdesc="Status bar for dwm"
url="https://github.com/57r4n63r/dwm-status.git"
provides=('dwm-status')
arch=('x86_64')
license=('MIT')
depends=('python3' 'python-pip' 'unzip')
makedepends=()
backup=()
install=''
source=(
	"lib.zip"
	"run.py"
	"dwm-status"
)

package() {
    install -d "$pkgdir"/opt
    install -d "$pkgdir"/opt/dwm-status

    unzip -o lib.zip

    cp -r ./Modules "$pkgdir"/opt/"$pkgname"
    cp -r ./Core "$pkgdir"/opt/"$pkgname"
    cp -Lr ./run.py "$pkgdir"/opt/"$pkgname"

    find "$pkgdir"/opt/"$pkgname"/ -type f -exec chmod 644 {} \;
    chmod 755 "$pkgdir"/opt/"$pkgname"

    install -d "$pkgdir"/usr/bin

    install -D -m755 "./dwm-status" "${pkgdir}/usr/bin/dwm-status"
}

md5sums=('9e43077c93a19b422dde5d5b88bfee72'
         'd4f3553b3ad870d92c5073c826862fcb'
         'a6457d02a29cc5b4517207e13246efe2')

