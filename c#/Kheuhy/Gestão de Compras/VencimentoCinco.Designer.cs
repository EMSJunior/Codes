namespace Gestão_de_Compras
{
    partial class VencimentoCinco
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dgvVencimentoCinco = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVencimentoCinco)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvVencimentoCinco
            // 
            this.dgvVencimentoCinco.AllowUserToAddRows = false;
            this.dgvVencimentoCinco.AllowUserToDeleteRows = false;
            this.dgvVencimentoCinco.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvVencimentoCinco.Location = new System.Drawing.Point(12, 1);
            this.dgvVencimentoCinco.Name = "dgvVencimentoCinco";
            this.dgvVencimentoCinco.ReadOnly = true;
            this.dgvVencimentoCinco.Size = new System.Drawing.Size(379, 267);
            this.dgvVencimentoCinco.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 293);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(137, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Venciemento em cinco dias";
            // 
            // VencimentoCinco
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(579, 329);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dgvVencimentoCinco);
            this.Name = "VencimentoCinco";
            this.Text = "VencimentoCinco";
            ((System.ComponentModel.ISupportInitialize)(this.dgvVencimentoCinco)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvVencimentoCinco;
        private System.Windows.Forms.Label label1;
    }
}