from pathlib import Path

content = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REKAP KAS MUDA-MUDI MASJID SEWERU</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        :root {
            --primary-color: #059669;
            --primary-dark: #064e3b;
            --accent-color: #10b981;
            --danger-color: #dc2626;
            --bg-color: #f3f4f6;
            --card-bg: #ffffff;
            --text-color: #1f2937;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            padding: 20px;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
            color: white;
            padding: 30px 22px;
            border-radius: 18px;
            box-shadow: 0 20px 40px rgba(5, 150, 105, 0.18);
        }

        header h1 {
            font-size: 28px;
            font-weight: 700;
            line-height: 1.2;
        }

        header p {
            font-size: 15px;
            margin-top: 10px;
            color: rgba(255, 255, 255, 0.92);
        }

        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 22px;
            box-shadow: 0 16px 30px rgba(15, 23, 42, 0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 6px solid var(--primary-color);
        }

        .card.pengeluaran {
            border-left-color: #ef4444;
        }

        .card.saldo {
            border-left-color: #3b82f6;
        }

        .card-info h3 {
            font-size: 14px;
            color: #6b7280;
            font-weight: 600;
        }

        .card-info p {
            font-size: 24px;
            font-weight: 700;
            margin-top: 8px;
            color: var(--text-color);
        }

        .card-icon {
            font-size: 34px;
            opacity: 0.25;
        }

        .card.pengeluaran .card-icon {
            color: #ef4444;
        }

        .card.saldo .card-icon {
            color: #3b82f6;
        }

        .notification {
            display: none;
            padding: 16px 18px;
            border-radius: 15px;
            margin-bottom: 24px;
            font-size: 14px;
            font-weight: 600;
            gap: 12px;
            align-items: center;
        }

        .notification.show {
            display: flex;
        }

        .notification.success {
            background-color: #dcfce7;
            color: #14532d;
            border: 1px solid #bbf7d0;
        }

        .notification.error {
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fecaca;
        }

        .main-content {
            display: grid;
            grid-template-columns: 1fr;
            gap: 24px;
        }

        @media (min-width: 768px) {
            .main-content {
                grid-template-columns: 360px 1fr;
            }
        }

        .form-section,
        .table-section {
            background: var(--card-bg);
            border-radius: 18px;
            padding: 26px;
            box-shadow: 0 18px 30px rgba(15, 23, 42, 0.06);
        }

        .form-section h2,
        .table-header h2 {
            font-size: 18px;
            color: var(--primary-dark);
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #374151;
            font-size: 13px;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 14px 15px;
            font-size: 14px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .form-group input:focus,
        .form-group select:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 4px rgba(5, 150, 105, 0.12);
            outline: none;
        }

        .btn-submit,
        .btn-reset,
        .btn-action {
            cursor: pointer;
            transition: transform 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
        }

        .btn-submit {
            width: 100%;
            padding: 14px 18px;
            border-radius: 14px;
            border: none;
            background-color: var(--primary-color);
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 14px 24px rgba(5, 150, 105, 0.16);
        }

        .btn-submit:hover {
            transform: translateY(-1px);
            background-color: var(--primary-dark);
        }

        .btn-reset {
            border: none;
            border-radius: 14px;
            padding: 12px 16px;
            color: #ffffff;
            background-color: var(--danger-color);
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-reset:hover {
            transform: translateY(-1px);
            background-color: #b91c1c;
        }

        .table-header {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }

        .table-header h2 {
            margin: 0;
        }

        .table-wrapper {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 700px;
        }

        th,
        td {
            padding: 14px 15px;
            border-bottom: 1px solid #e5e7eb;
            font-size: 14px;
        }

        th {
            background-color: #f8fafc;
            color: #4b5563;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        tr:hover {
            background-color: #f8fafc;
        }

        .text-pemasukan {
            color: #047857;
            font-weight: 700;
        }

        .text-pengeluaran {
            color: #b91c1c;
            font-weight: 700;
        }

        .text-saldo {
            color: #065f46;
            font-weight: 700;
        }

        .text-empty {
            color: #6b7280;
        }

        .action-group {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .btn-action {
            border: 1px solid transparent;
            border-radius: 10px;
            padding: 9px 12px;
            font-size: 13px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-action.edit {
            background-color: #ecfdf5;
            color: #065f46;
            border-color: #6ee7b7;
        }

        .btn-action.delete {
            background-color: #fef2f2;
            color: #991b1b;
            border-color: #fca5a5;
        }

        .btn-action:hover {
            transform: translateY(-1px);
        }

        @media (max-width: 767px) {
            body {
                padding: 14px;
            }

            header {
                padding: 24px 16px;
            }

            .form-section,
            .table-section {
                padding: 20px;
            }

            th,
            td {
                padding: 12px 10px;
            }

            .btn-submit,
            .btn-reset {
                width: 100%;
            }

            .table-wrapper {
                overflow-x: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>REKAP KAS MUDA-MUDI MASJID SEWERU</h1>
            <p><i class="fa-solid fa-mosque"></i> Kelola kas muda-mudi secara modern, aman, dan langsung tersimpan di browser.</p>
        </header>

        <div id="notification" class="notification"></div>

        <div class="dashboard">
            <div class="card">
                <div class="card-info">
                    <h3>Total Pemasukan</h3>
                    <p id="total-pemasukan">Rp0</p>
                </div>
                <div class="card-icon"><i class="fa-solid fa-hand-holding-dollar"></i></div>
            </div>
            <div class="card pengeluaran">
                <div class="card-info">
                    <h3>Total Pengeluaran</h3>
                    <p id="total-pengeluaran">Rp0</p>
                </div>
                <div class="card-icon"><i class="fa-solid fa-file-invoice-dollar"></i></div>
            </div>
            <div class="card saldo">
                <div class="card-info">
                    <h3>Sisa Kas Akhir Tahun</h3>
                    <p id="sisa-kas">Rp0</p>
                </div>
                <div class="card-icon"><i class="fa-solid fa-wallet"></i></div>
            </div>
        </div>

        <div class="main-content">
            <div class="form-section">
                <h2><i class="fa-solid fa-pen-to-square"></i> Input & Edit Data</h2>
                <form id="kas-form">
                    <div class="form-group">
                        <label for="tahun">Tahun</label>
                        <select id="tahun" required></select>
                    </div>
                    <div class="form-group">
                        <label for="bulan">Bulan</label>
                        <select id="bulan" required>
                            <option value="Januari">Januari</option>
                            <option value="Februari">Februari</option>
                            <option value="Maret">Maret</option>
                            <option value="April">April</option>
                            <option value="Mei">Mei</option>
                            <option value="Juni">Juni</option>
                            <option value="Juli">Juli</option>
                            <option value="Agustus">Agustus</option>
                            <option value="September">September</option>
                            <option value="Oktober">Oktober</option>
                            <option value="November">November</option>
                            <option value="Desember">Desember</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="pemasukan">Pemasukan (Rp)</label>
                        <input type="number" id="pemasukan" min="0" step="1" placeholder="Contoh: 250000" required>
                    </div>
                    <div class="form-group">
                        <label for="pengeluaran">Pengeluaran (Rp)</label>
                        <input type="number" id="pengeluaran" min="0" step="1" placeholder="Contoh: 50000" required>
                    </div>
                    <button type="submit" class="btn-submit" id="submit-button"><i class="fa-solid fa-floppy-disk"></i> Simpan Data</button>
                </form>
            </div>

            <div class="table-section">
                <div class="table-header">
                    <h2><i class="fa-solid fa-list-check"></i> Tabel Rekap Tahunan</h2>
                    <button type="button" class="btn-reset" id="reset-button"><i class="fa-solid fa-trash"></i> Reset Data</button>
                </div>
                <div class="table-wrapper">
                    <table id="kas-table">
                        <thead>
                            <tr>
                                <th>Bulan</th>
                                <th>Pemasukan</th>
                                <th>Pengeluaran</th>
                                <th>Sisa Kas</th>
                                <th>Aksi</th>
                            </tr>
                        </thead>
                        <tbody id="table-body"></tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script>
        const listBulan = [
            'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
            'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
        ];

        const storageKey = 'sistemRekapKasSeweru';
        let dbKas = JSON.parse(localStorage.getItem(storageKey) || '{}');
        let editKey = null;

        const form = document.getElementById('kas-form');
        const selectTahun = document.getElementById('tahun');
        const selectBulan = document.getElementById('bulan');
        const inputPemasukan = document.getElementById('pemasukan');
        const inputPengeluaran = document.getElementById('pengeluaran');
        const submitButton = document.getElementById('submit-button');
        const tableBody = document.getElementById('table-body');
        const notification = document.getElementById('notification');
        const resetButton = document.getElementById('reset-button');

        const currentYear = new Date().getFullYear();
        const tahunOptions = [currentYear - 1, currentYear, currentYear + 1, currentYear + 2];

        function initYearOptions() {
            selectTahun.innerHTML = tahunOptions
                .map(tahun => `<option value="${tahun}">${tahun}</option>`)
                .join('');
            selectTahun.value = currentYear;
        }

        function showNotification(message, type = 'success') {
            notification.textContent = message;
            notification.className = `notification show ${type}`;
            clearTimeout(notification.hideTimeout);
            notification.hideTimeout = setTimeout(() => {
                notification.className = 'notification';
            }, 3200);
        }

        function formatRupiah(value) {
            const number = Number(value);
            if (Number.isNaN(number)) {
                return 'Rp0';
            }
            return new Intl.NumberFormat('id-ID', {
                style: 'currency',
                currency: 'IDR',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            }).format(number);
        }

        function saveStorage() {
            localStorage.setItem(storageKey, JSON.stringify(dbKas));
        }

        function clearForm() {
            form.reset();
            editKey = null;
            submitButton.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Simpan Data';
            submitButton.classList.remove('edit-mode');
        }

        function validateInput(tahun, bulan, pemasukan, pengeluaran) {
            if (!tahun || !bulan) {
                showNotification('Tahun dan bulan harus dipilih.', 'error');
                return false;
            }
            if (String(inputPemasukan.value).trim() === '' || String(inputPengeluaran.value).trim() === '') {
                showNotification('Pemasukan dan pengeluaran wajib diisi.', 'error');
                return false;
            }
            if (!Number.isInteger(pemasukan) || !Number.isInteger(pengeluaran)) {
                showNotification('Nilai pemasukan dan pengeluaran harus berupa angka bulat.', 'error');
                return false;
            }
            if (pemasukan < 0 || pengeluaran < 0) {
                showNotification('Nilai angka tidak boleh negatif.', 'error');
                return false;
            }
            return true;
        }

        function renderTable() {
            const tahunDipilih = selectTahun.value;
            tableBody.innerHTML = '';

            let totalPemasukan = 0;
            let totalPengeluaran = 0;
            let saldoSebelumnya = 0;
            let adaData = false;

            listBulan.forEach(bulan => {
                const key = `${tahunDipilih}-${bulan}`;
                const data = dbKas[key];
                const hasData = Boolean(data);
                const pemasukan = hasData ? data.pemasukan : 0;
                const pengeluaran = hasData ? data.pengeluaran : 0;

                saldoSebelumnya = saldoSebelumnya + pemasukan - pengeluaran;

                if (hasData) {
                    totalPemasukan += pemasukan;
                    totalPengeluaran += pengeluaran;
                    adaData = true;
                }

                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><strong>${bulan} ${tahunDipilih}</strong></td>
                    <td class="${hasData ? 'text-pemasukan' : 'text-empty'}">${hasData ? formatRupiah(pemasukan) : '-'}</td>
                    <td class="${hasData ? 'text-pengeluaran' : 'text-empty'}">${hasData ? formatRupiah(pengeluaran) : '-'}</td>
                    <td class="text-saldo">${formatRupiah(saldoSebelumnya)}</td>
                    <td>
                        ${hasData ? `
                            <div class="action-group">
                                <button type="button" class="btn-action edit" onclick="editEntry('${key}')"><i class="fa-solid fa-pen"></i> Edit</button>
                                <button type="button" class="btn-action delete" onclick="deleteEntry('${key}')"><i class="fa-solid fa-trash"></i> Hapus</button>
                            </div>
                        ` : '<span class="text-empty">-</span>'}
                    </td>
                `;
                tableBody.appendChild(row);
            });

            if (!adaData) {
                const emptyRow = document.createElement('tr');
                emptyRow.innerHTML = `
                    <td colspan="5" class="text-empty" style="text-align:center; padding: 32px 10px;">Belum ada data kas untuk tahun ${tahunDipilih}. Tambahkan data bulan terlebih dahulu.</td>
                `;
                tableBody.appendChild(emptyRow);
            }

            document.getElementById('total-pemasukan').innerText = formatRupiah(totalPemasukan);
            document.getElementById('total-pengeluaran').innerText = formatRupiah(totalPengeluaran);
            document.getElementById('sisa-kas').innerText = formatRupiah(saldoSebelumnya);
        }

        function editEntry(key) {
            const data = dbKas[key];
            if (!data) {
                showNotification('Data untuk diedit tidak ditemukan.', 'error');
                return;
            }
            const [tahun, bulan] = key.split('-');
            selectTahun.value = tahun;
            selectBulan.value = bulan;
            inputPemasukan.value = data.pemasukan;
            inputPengeluaran.value = data.pengeluaran;
            editKey = key;
            submitButton.innerHTML = '<i class="fa-solid fa-pen-to-square"></i> Perbarui Data';
            submitButton.classList.add('edit-mode');
            renderTable();
        }

        function deleteEntry(key) {
            if (!dbKas[key]) {
                showNotification('Data untuk dihapus tidak ditemukan.', 'error');
                return;
            }
            const [tahun, bulan] = key.split('-');
            if (confirm(`Hapus data ${bulan} ${tahun}? Tindakan ini tidak dapat dibatalkan.`)) {
                delete dbKas[key];
                saveStorage();
                if (editKey === key) {
                    clearForm();
                }
                renderTable();
                showNotification(`Data ${bulan} ${tahun} berhasil dihapus.`, 'success');
            }
        }

        function resetData() {
            if (confirm('Apakah Anda yakin ingin menghapus seluruh data kas?')) {
                dbKas = {};
                saveStorage();
                clearForm();
                renderTable();
                showNotification('Seluruh data kas berhasil direset.', 'success');
            }
        }

        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const tahun = selectTahun.value;
            const bulan = selectBulan.value;
            const pemasukan = Number(inputPemasukan.value);
            const pengeluaran = Number(inputPengeluaran.value);

            if (!validateInput(tahun, bulan, pemasukan, pengeluaran)) {
                return;
            }

            const newKey = `${tahun}-${bulan}`;
            if (editKey && editKey !== newKey && dbKas[newKey]) {
                showNotification(`Data untuk ${bulan} ${tahun} sudah ada. Gunakan bulan lain atau batalkan edit.`, 'error');
                return;
            }

            if (editKey && editKey !== newKey) {
                delete dbKas[editKey];
            }

            dbKas[newKey] = {
                pemasukan,
                pengeluaran
            };
            saveStorage();
            renderTable();
            const message = editKey ? `Data ${bulan} ${tahun} berhasil diperbarui.` : `Data ${bulan} ${tahun} berhasil disimpan.`;
            clearForm();
            showNotification(message, 'success');
        });

        selectTahun.addEventListener('change', renderTable);
        resetButton.addEventListener('click', resetData);

        window.editEntry = editEntry;
        window.deleteEntry = deleteEntry;

        initYearOptions();
        renderTable();
    </script>
</body>
</html>
'''
Path('kas-baru.html').write_text(content, encoding='utf-8')
"