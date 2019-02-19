# Maintainer: David-Alexandre Rancourt <david.a.rancourt@gmail.com>

pkgname=dwm-status
pkgrel=1
pkgver=1.0.0
pkgdesc="Status bar for dwm"
url="https://github.com/57r4n63r/dwm-status.git"
provides=('dwm-status')
arch=('x86_64')
license=('MIT')
depends=('python3' 'python-pip')
makedepends=()
backup=()
install=''
source=(
	"StatusBar.py"
	"exec.py"
	"icons.json"
	"dwm-status"
)

package() {
    install -d "$pkgdir"/opt
    install -d "$pkgdir"/opt/dwm-status
    cp ./StatusBar.py "$pkgdir"/opt/"$pkgname"
    cp ./exec.py "$pkgdir"/opt/"$pkgname"
    cp ./icons.json "$pkgdir"/opt/"$pkgname"

    find "$pkgdir"/opt/"$pkgname"/ -type f -exec chmod 644 {} \;
    chmod 755 "$pkgdir"/opt/"$pkgname"

    install -d "$pkgdir"/usr/bin

    install -D -m755 "./dwm-status" "${pkgdir}/usr/bin/dwm-status"
}

md5sums=('896012adc07ddaad6bf186a300baca70'
         '5c1d890914060a9c30dad9433383a672'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('09fdbe0cd04d1490071ad2336c2be1cf'
         '5c1d890914060a9c30dad9433383a672'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('09fdbe0cd04d1490071ad2336c2be1cf'
         '5c1d890914060a9c30dad9433383a672'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('081f52557f4325125b0057622c2e4e10'
         '5c1d890914060a9c30dad9433383a672'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('45e73a1663c65979be86f2faae140f91'
         '5c1d890914060a9c30dad9433383a672'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('2a191cd8c53f6380b14339c1e6f11544'
         '0f20a58f0b178e93c98aeaa61d677845'
         '9df861e848da2ac2ee00e1992f872a09'
         '6fc29520560e73de2ee147111af6a4c8')
md5sums=('2a191cd8c53f6380b14339c1e6f11544'
         '0f20a58f0b178e93c98aeaa61d677845'
         '9df861e848da2ac2ee00e1992f872a09'
         'd36eb3ceb40d87669bf39122170114c7')
