//
//  LoginViewController.swift
//  LiveHive
//
//  Created by Brianna Butler on 8/20/20.
//  Copyright © 2020 LiveHive. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    @IBOutlet weak var usernameField: UITextField!
    
    @IBOutlet weak var passwordField: UITextField!
    
    var imageView = UIImageView(frame: CGRect(x: 1, y: 0, width: 5, height: 5))
    
    var passimageView = UIImageView(frame: CGRect(x: 1, y: 0, width: 0.5, height: 0.5))
    
    var image = UIImage(named: "user.png")
    
    var passimage = UIImage(named: "lock.png")
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
        
        /*imageView.contentMode = .scaleAspectFit
        
        imageView.image = image
        
        imageView.alpha = 0.4
        
        usernameField.leftView = imageView
        
        usernameField.leftViewMode = UITextField.ViewMode.always

        usernameField.leftViewMode = .always
        
        passimageView.contentMode = .scaleAspectFit
        
        passimageView.image = passimage
        
        passimageView.alpha = 0.4
        
        passwordField.leftView = passimageView
        
        passwordField.leftViewMode = UITextField.ViewMode.always

        passwordField.leftViewMode = .always*/
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
